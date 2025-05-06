from datetime import datetime,timedelta

def get_sympton_input(sympton):
    result=input(f" do you have {sympton} ? (yes/no) : ").strip().lower()
    if result=="yes":
        days=int(input(f"how many days have you had {sympton} : "))
        return True,days
    return False,0

def diagnosis(symptons):

    if symptons['fever'][0] and  symptons['runny_nose'][0] and symptons['sore_throat'][0]:
        return "common cold",["paracetamol","stay hydrated","take rest"],"no blood test needed"

    elif symptons['fever'][0] and symptons['headache'][0] and symptons['chills'][0] and symptons['dizziness']:
        return "Maleria", ["Antibiotics", "in wrost case : get admitted", "take rest"], ["blood test needed","CBC","urine test"]

    elif symptons['vomiting'][0] and symptons['stomach_ache'][0] and symptons['diarrhea'][0]:
        return "Food poisoning", ["antibiotics", "avoid solid food", "take rest"], ["blood test needed"]

    else:
        return "unknown symptons", ["consult an MD Doctor"], ["blood test","urine test","CBC"]

def scheduling_next_appointment():
    today=datetime.today()
    next_date=today + timedelta(days=3)
    return next_date.strftime('%d-%m-%y')




