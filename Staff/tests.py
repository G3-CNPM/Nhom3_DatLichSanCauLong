from django.test import TestCase, Client
from django.urls import reverse
from .models import Course, Student

class ViewsTestCase(TestCase):
  def setUp(self):
    self.client = Client()
    self.course = Course.objects.create(name="Test Course")
    self.student = Student.objects.create(name="Test Student")

  def test_home_view(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'home.html')

  def test_courses_view(self):
    response = self.client.get(reverse('courses'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'app_home/course/courses.html')
    self.assertContains(response, self.course.name)

  def test_edit_course_view(self):
    response = self.client.get(reverse('edit_course', args=[self.course.id]))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'app_home/course/course-edit.html')
    self.assertContains(response, self.course.name)

  def test_delete_course_view(self):
    response = self.client.get(reverse('delete_course', args=[self.course.id]))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'app_home/course/course-delete.html')
    self.assertContains(response, self.course.name)

  def test_students_view(self):
    response = self.client.get(reverse('students'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'app_home/student/students.html')
    self.assertContains(response, self.student.name)

  def test_student_edit_view(self):
    response = self.client.get(reverse('studentEdit', args=[self.student.id]))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'app_home/student/student-edit.html')
    self.assertContains(response, self.student.name)

  def test_student_delete_view(self):
    response = self.client.get(reverse('studentDelete', args=[self.student.id]))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'app_home/student/student-delete.html')
    self.assertContains(response, self.student.name)

  def test_student_new_view(self):
    response = self.client.get(reverse('studentNew'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'app_home/student/student-new.html')

  def test_course_new_view(self):
    response = self.client.get(reverse('CourseNew'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'app_home/course/course-new.html')