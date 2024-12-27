from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
from django.http import JsonResponse
from .rag_services import RAGService
from django.shortcuts import render


rag_service = RAGService()

# Load and prepare data at startup
docs = rag_service.prepare_data([
    "https://www.sfhsa.org/services/housing",
    "https://www.sfinterfaithcouncil.org/homeless-resources",
    "https://www.projecthomelessconnect.org/",
    "https://www.projecthomelessconnect.org/volunteer/",
    "https://projects.sfchronicle.com/sf-homeless/how-to-help/",
    "https://www.homeaway.org/",
    "https://abode.org/",
    "https://www.projecthomelessconnect.org/2020/04/available-services-guide/",
    #Adding manually
    "https://cots.org/ways-to-give-2/",

    #end for testing
    "https://abode.org/",
    "https://www.ahoproject.org/",
    "https://backonmyfeet.org/san-francisco",
    "https://www.bayarearescue.org/",
    "https://insighthousing.org/",
    "https://beyondemancipation.org/",
    "https://bfwc.org/",
    "https://www.self-sufficiency.org/",
    "https://catholiccharitiessf.org/",
    "https://www.cceb.org/",
    "https://www.carethroughtouch.org/",
    "https://charlottemaxwell.org/",
    "https://www.cityteam.org/",
    "https://www.cohsf.org/",
    "https://cots.org/",

])
rag_service.initialize_vectorstore(docs)

def home(request):
    return render(request,'rag_services/index.html')
def rag_query_view(request):
    question = request.GET.get("question", "")
    if not question:
        return JsonResponse({"error": "Please provide a question."}, status=400)
    response = rag_service.query_rag(question)
    return JsonResponse({"response": response})




# What if the question I am looking for I don't have in the database