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
    "http://welcomehomesf.org",
    "https://www.urbanangelssf.org/",
    "http://sanfrancisco.salvationarmy.org",
    "http://thegubbioproject.org",
    "https://tndc.org",
    "https://www.swords-to-plowshares.org/",
    "https://svdp-sf.org/",
    "http://stanthonysf.org/volunteer",
    "http://simplythebasics.org",
    "https://sfnightministry.org",
    "http://sfmfoodbank.org",
    "http://raphaelhouse.org",
    "http://prcsf.org",
    "http://northbeachcitizens.org/take-action",
    "http://miraclemessages.org",
    "https://www.mercyhousing.org/california/",
    "http://martindeporres.org",
    "http://lssnorcal.org",
    "http://larkinstreetyouth.org",
    "http://lavozlatinasf.org",
    "https://www.lavamaex.org?",
    "http://lacasa.org",
    "http://hcnkids.org",
    "http://healthright360.org",
    "http://healingwellsf.org",
    "http://hamiltonfamilies.org",
    "https://hills.ccsf.edu/~eandrew6/foodprogram/whoweare.htm",
    "http://glide.org",
    "http://foodrunners.org",
    "http://farminghope.org",
    "https://ecs-sf.org",
    "http://streetsteam.org",
    "http://dscs.org",
    "http://dishsf.org",
    "http://curryseniorcenter.org/volunteer",
    "http://compass-sf.org",
    "http://chp-sf.org",
    "http://cohsf.org",
    "http://carethroughtouch.org",
    "http://catholiccharitiessf.org",
    "https://backonmyfeet.org/san-francisco",
    "https://www.sf.gov/reports/december-2024/overdose-prevention-plan-2024?_gl=1%2Auakbj2%2A_ga%2ANzU0ODAwMTY5LjE3MzM0MzY5Nzk.%2A_ga_BT9NDE0NFC%2AMTczNTMzOTk0OC4zLjEuMTczNTM0MDI3My4wLjAuMA..%2A_ga_63SCS846YP%2AMTczNTMzOTk0OC4zLjEuMTczNTM0MDI3My4wLjAuMA..",
    "https://www.aa.org/",
    "https://www.sf.gov/information/addiction-and-detox-treatment",
    "https://aasfmarin.org/",
    "https://www.sf.gov/get-birth-certificate-someone-over-3",
    "https://www.sfhsa.org/services/jobs-money/jobsnow",
    "https://www.sf.gov/get-job-and-career-services",
    "https://www.sfhsa.org/services/financial-assistance/county-adult-assistance-programs-caap",
    "https://calcountylawlib.libguides.com/legalservices",
    "https://www.sfserviceguide.org/hygiene-resources/form",
    "https://sfserviceguide.org/search?query=laundry",
    "https://www.sfdph.org/dph/comupg/oservices/medSvs/dentalSvcs/dentalClinics.asp",
    "https://sf.gov/topics/health?_gl=1*z0xpjh*_ga*NzU0ODAwMTY5LjE3MzM0MzY5Nzk.*_ga_BT9NDE0NFC*MTczNTMzOTk0OC4zLjEuMTczNTM0MDQxMy4wLjAuMA..*_ga_63SCS846YP*MTczNTMzOTk0OC4zLjEuMTczNTM0MDQxMy4wLjAuMA..",
    "http://www.mhbsf.org/resources/#mental",
    "https://sf.gov/resource/2022/sf-health-network-clinics?_gl=1*wk8oi1*_ga*NzU0ODAwMTY5LjE3MzM0MzY5Nzk.*_ga_BT9NDE0NFC*MTczNTMzOTk0OC4zLjEuMTczNTM0MDQxMy4wLjAuMA..*_ga_63SCS846YP*MTczNTMzOTk0OC4zLjEuMTczNTM0MDQxMy4wLjAuMA..",
    "https://www.sf.gov/departments/department-public-health/behavioral-health",
    "https://housing.sfgov.org/",
    "https://hsh.sfgov.org/services/how-to-get-services/accessing-temporary-shelter/",
    "https://hsh.sfgov.org/about/how-to-get-involved/",
    "https://www.sf.gov/reentry-transitional-and-supportive-housing#:~:text=The%20Billie%20Holiday%20Center%20(BHC,the%20San%20Francisco%20County%20Jail.",
    "https://www.sfserviceguide.org/services/1649",
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