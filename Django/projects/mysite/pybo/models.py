from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 제목은 최대 200자까지
    content = models.TextField()  # 내용은 제한 없는 텍스트
    create_date = models.DateTimeField()  # 날짜 및 시간 정보 저장

    def __str__(self):
        return self.subject
    
class Answer(models.Model):  
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 기존 속성 연결 - ForeignKey
    # on_delete=models.CASCADE 이 답변이 연결된 질문이 삭제되면, 해당 답변도 함께 삭제됨. 

    content = models.TextField()
    create_date = models.DateTimeField()
    
