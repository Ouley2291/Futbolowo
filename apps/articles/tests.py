import tempfile
from django.test import TestCase, Client, override_settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Article, Comment
from .forms import CreateArtcileForm, EditArticleForm, CommentForm

# Tworzenie tymczasowego katalogu na pliki mediów podczas testów
TEMP_MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class ArticleViewTests(TestCase):
    """Testy dla funkcji views.py w aplikacji articles"""

    def setUp(self):
        """Konfiguracja danych testowych dla wszystkich testów widoków"""
        self.client = Client()
        
        # Tworzenie urzytkowników z różnymi poziomami uprawnień
        self.staff_user = User.objects.create_user(
            username="admin1", password="admin2", is_staff=True
        )
        self.regular_user = User.objects.create_user(
            username="user", password="Password123.,", is_staff=False
        )

        # 1x1 GIF wykorzystywany jako miniatura do testów
        self.small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        self.thumbnail = SimpleUploadedFile("thumb.gif", self.small_gif, content_type="image/gif")

        # Tworzenie artykułu początkowego w bazie danych
        self.article = Article.objects.create(
            title="Initial Article",
            creator=self.staff_user,
            category="Transfery",
            content="Content of the initial article",
            thumbnail=self.thumbnail
        )

    # TESTY: add (Dodawanie artykułów)

    def test_add_view_anonymous_redirects(self):
        """Niezalogowany użytkownik powinien zostać przekierowany do formularza logowania przy próbie wejścia na stronę dodawania"""
        response = self.client.get(reverse("articles:add"))
        self.assertRedirects(response, f"/login/?next={reverse('articles:add')}")

    def test_add_view_non_staff_redirects(self):
        """Zalogowany zwykły użytkownik (niebędący staffem) przy próbie wejścia na dodawanie powinien zostać przekierowany na stronę główną"""
        self.client.login(username="user", password="Password123.,")
        response = self.client.get(reverse("articles:add"))
        self.assertRedirects(response, reverse("core:index"))


    # TESTY: edit (Edycja artykułów)

    def test_edit_view_anonymous_redirects(self):
        """Niezalogowany użytkownik próbujący edytować artykuł powinien zostać przekierowany do formularza logowania"""
        response = self.client.get(reverse("articles:edit", kwargs={"id": self.article.id}))
        self.assertRedirects(response, f"/login/?next={reverse('articles:edit', kwargs={'id': self.article.id})}")

    def test_edit_view_non_staff_redirects(self):
        """Zalogowany zwykły użytkownik próbujący edytować artykuł powinien zostać przekierowany do widoku szczegółów tego artykułu"""
        self.client.login(username="user", password="Password123.,")
        response = self.client.get(reverse("articles:edit", kwargs={"id": self.article.id}))
        self.assertRedirects(response, reverse("articles:view", kwargs={"id": self.article.id}))

    # TESTY: article_view (Szczegóły i Komentarze)

    def test_article_view_get(self):
        """GET na szczegóły artykułu powinien wyświetlić artykuł, powiązane komentarze oraz formularz nowego komentarza"""
        comment = Comment.objects.create(
            author=self.regular_user,
            article=self.article,
            content="Bardzo ciekawy artykuł!"
        )
        response = self.client.get(reverse("articles:view", kwargs={"id": self.article.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "articles/article_view.html")
        self.assertEqual(response.context["article"], self.article)
        self.assertIn(comment, response.context["comments"])
        self.assertIsInstance(response.context["form"], CommentForm)

    def test_article_view_post_comment_authenticated(self):
        """Zalogowany użytkownik powinien pomyślnie dodać komentarz przez POST i zostać przekierowany z powrotem do artykułu"""
        self.client.login(username="user", password="Password123.,")
        post_data = {
            "content": "Kolejny komentarz testowy"
        }
        response = self.client.post(reverse("articles:view", kwargs={"id": self.article.id}), data=post_data)
        
        # Powinno nastąpić przekierowanie z powrotem na szczegóły artykułu
        self.assertRedirects(response, reverse("articles:view", kwargs={"id": self.article.id}))
        
        # Sprawdzenie czy komentarz został zapisany i przypisany do odpowiedniego artykułu oraz autora
        comment = Comment.objects.get(content="Kolejny komentarz testowy")
        self.assertEqual(comment.author, self.regular_user)
        self.assertEqual(comment.article, self.article)

    # TESTY: article_list (Lista artykułów)

    def test_article_list_all(self):
        """Widok listy artykułów powinien zwrócić status 200 i poprawnie posortować artykuły od najnowszego"""
        # Tworzenie drugiego artykułu (będzie nowszy z racji późniejszego dodania)
        new_thumb = SimpleUploadedFile("thumb2.gif", self.small_gif, content_type="image/gif")
        another_article = Article.objects.create(
            title="Second Article",
            creator=self.staff_user,
            category="Mecze",
            content="Content 2",
            thumbnail=new_thumb
        )
        
        response = self.client.get(reverse("articles:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "articles/article_list.html")
        
        articles_in_context = list(response.context["articles"])
        self.assertEqual(len(articles_in_context), 2)
        
        # Najnowszy artykuł powinien być pierwszy na liście
        self.assertEqual(articles_in_context[0], another_article)
        self.assertEqual(articles_in_context[1], self.article)