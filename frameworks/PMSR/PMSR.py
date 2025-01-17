import json

import constants as _C
from utils.Config import Config
from frameworks.Framework import Framework

class PMSR(Framework):
    def __init__(self, data):
        super().__init__(data)
        pass
    
    def gateCheck(self):
        cliParams = Config.get('_SS_PARAMS')
        if 'others' in cliParams and not cliParams['others'] == None:
            requestId = cliParams['others']
            return self.checkIfFollowFRID(requestId)
        
        return False
        
    def checkIfFollowFRID(self, requestId):
        raws = requestId.split('-')
        if len(raws) == 5 and raws[0] == 'F':
            return True
            
        return False
    
if __name__ == "__main__":
    data = json.loads(open(_C.FRAMEWORK_DIR + '/api.json').read())
    # print(data)
    o = PMSR(data)
    o.readFile()
    # o.obj()
    o.generateMappingInformation()