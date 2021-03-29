class basicunit :


    def  __init__ (self, myCampId,myFacId,myDeptId,myProgId,myProgOptionId,myAsetId,myAsessionId,mySemesterId,myLevelTodo,myCourseId):
        
        self.myCampId=myCampId
        self.myFacId=myFacId
        self.myDeptId=myDeptId
        self.myProgId=myProgId
        self.myProgOptionId=myProgOptionId
        self.myAsetId=myAsetId
        self.myAsessionId=myAsessionId
        self.mySemesterId=mySemesterId
        self.myLevelTodo=myLevelTodo
        self.myCourseId=myCourseId

class MergebasicScorelist:
    def __init__(self, basicdata,scores):

        self.basicdata=basicdata
        self.scores=scores
        