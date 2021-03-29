from .models import AvailableSemester


def filterUnAvailableSemesters(courselist):
    availabuSemesters = AvailableSemester.objects.all();
    newcourselist=[]
    print(list(availabuSemesters))
    for crs in courselist:
            #print (crs)
            #print (crs[""])
            for i in list(availabuSemesters):
                print(i.myCampId,'---',crs['MYCAMPID'] )
                print(i.myCampId,crs['MYCAMPID'] , i.myProgId,crs['MYPROGID'] , i.myAsetId,crs['MYASETID'] , i.myAsessionId,crs['MYASESSIONID'] , i.mySemesterId,crs['MYSEMESTERID'] , i.myTheprogType,crs['MYTHEPROG'] )
                if i.myCampId==crs['MYCAMPID'] and i.myProgId==crs['MYPROGID'] and i.myAsetId==crs['MYASETID'] and i.myAsessionId==crs['MYASESSIONID'] and i.mySemesterId==crs['MYSEMESTERID'] and i.myTheprogType==crs['MYTHEPROG'] :
                   
                   newcourselist.append(crs)
    print('seeeeeeeeeeeeeeeeeeeeeee')  
    print(newcourselist)
    return(newcourselist)
