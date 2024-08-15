from . models import CustomUser
from home.models import UserMedicalData, UserPersonalData


def CheckPersonalData(request):
    user = request.user
    ispersonaldata = UserPersonalData.objects.filter(user = user).first()
    if ispersonaldata:
        return isinstance
    else:
        return False



def CheckMedicalData(request):
    user = request.user
    ismedicaldata = UserMedicalData.objects.filter(user = user).first()
    if ismedicaldata:
        return ismedicaldata
    else:
        return False
    




# def CheckDeitryData(request)

    