from rest_framework import status
from rest_framework.test import APITestCase

from studies.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@gmail.com',
            password='test'
        )
        self.user.is_superuser = True
        self.user.save()

        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """Тест для создания урока"""

        data = {
            'name': 'test for create',
            'description': 'test for create',
            'link_to_video': 'https://www.youtube.com/'
        }

        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1,
             'name': 'test for create',
             'description': 'test for create',
             'course': None,
             'link_to_video': 'https://www.youtube.com/',
             'preview': None,
             'owner': 1}
        )

    def test_list_lessons(self):
        """Тест получения списка уроков"""

        lesson = Lesson.objects.create(
            name='test for list',
            description='test for list',
            link_to_video='https://www.youtube.com/'
        )

        response = self.client.get(
            '/lesson/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': lesson.pk,
                            'name': 'test for list',
                            'description': 'test for list',
                            'course': None,
                            'link_to_video': 'https://www.youtube.com/',
                            'preview': None,
                            'owner': None
                        }
                    ]
            }

        )

    def test_detail_lesson(self):
        """Тест детального просмотра урока"""
        lesson = Lesson.objects.create(
            name='details test',
            description='details test',
            link_to_video='https://www.youtube.com/'
        )
        response = self.client.get(f'/lesson/detail/{lesson.pk}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': lesson.pk,
                'name': 'details test',
                'description': 'details test',
                'course': None,
                'link_to_video': 'https://www.youtube.com/',
                'preview': None,
                'owner': None
            }

        )

    def test_update_lesson(self):
        """Тест для обновления урока"""
        lesson = Lesson.objects.create(
            name='test for update',
            description='test for update',
            link_to_video='https://www.youtube.com/'
        )

        updated_data = {
            'name': 'updated title',
            'description': 'updated description',
            'link_to_video': 'https://www.youtube.com/'
        }

        response = self.client.put(
            f'/lesson/update/{lesson.pk}/',
            data=updated_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': lesson.pk,
                'name': 'updated title',
                'description': 'updated description',
                'preview': None,
                'link_to_video': 'https://www.youtube.com/',
                'course': None,
                'owner': None
            }
        )

    def test_delete_lesson(self):
        """Тест для удаления урока"""
        lesson = Lesson.objects.create(
            name='test for delete',
            description='test for delete',
            link_to_video='https://www.youtube.com/'
        )

        response = self.client.delete(
            f'/lesson/delete/{lesson.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )