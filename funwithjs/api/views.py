from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response

from .models import TopicList, QuestionList
from .serializer import TopicListSerializer, QuestionListSerializer

# Create your views here.
class TopicListAPI(APIView):
    queryset = TopicListSerializer
    questAns = QuestionListSerializer
    def get(self, request, id=None, format=None):
        try:
            if id is not None:
                stu = TopicList.objects.get(id=id)
                quer_ans = QuestionList.objects.filter(topic_id=id)
                serializer = self.queryset(stu)
                serializer_question_answer = self.questAns(quer_ans, many=True)
                return  Response({"data": serializer.data, "quesAns":serializer_question_answer.data, "msg": "This is get request"})
            stu = TopicList.objects.all()
            serializer = self.queryset(stu, many=True)
            return  Response({"data": serializer.data, "msg": "This is get request"})
        except Exception as  error:
            return  Response({"error": error,"status": status.HTTP_404_NOT_FOUND})

    def post(self, request, format=None):
        serializer = self.queryset(data =request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'message': "data added"}
            return Response(res, status=status.HTTP_201_CREATED)
                    
        return Response({"error": serializer.errors,"status":status.HTTP_400_BAD_REQUEST})

    def put(self, request, id, format=None):
        try:            
            stu= TopicList.objects.get(id=id)
            serializer = self.queryset(stu, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "updated"})
            return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)
        except Exception as  error:
            return  Response({"error": error,"status": status.HTTP_404_NOT_FOUND})

    
    def delete(self, request, id, format=None):
        stu = TopicList.objects.get(id=id)
        stu.delete()
        return Response({"msg":"Record Deleted"})

class QuestionListAPI(APIView):

    def get(self, request, id=None, format=None):
        try:
            if id is not None:
                stu = QuestionList.objects.get(id=id)
                print(stu, "dataaa")
                serializer = QuestionListSerializer(stu)
                return  Response({"data": serializer.data, "msg": "This is get request"})
            stu = QuestionList.objects.all()
            serializer = QuestionListSerializer(stu, many=True)
            return  Response({"data": serializer.data, "msg": "This is get request"})
        except Exception as  error:
            return  Response({"error": error,"status": status.HTTP_404_NOT_FOUND})

    def post(self, request, format=None):
        serializer = QuestionListSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'message': "data added"}
            return Response(res, status=status.HTTP_201_CREATED)
                    
        return Response({"error": serializer.errors,"status":status.HTTP_400_BAD_REQUEST})

    def put(self, request, id, format=None):
        try:            
            stu= QuestionList.objects.get(id=id)
            serializer = QuestionListSerializer(stu, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "updated"})
            return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)
        except Exception as  error:
            return  Response({"error": error,"status": status.HTTP_404_NOT_FOUND})
    
    def delete(self, request, id, format=None):
        stu = QuestionList.objects.get(id=id)
        stu.delete()
        return Response({"msg":"Record Deleted"})