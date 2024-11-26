import tempfile
import os
import subprocess


class SecurityCheck():

    def __init__(self, raw_code):
        self.raw_code = raw_code

    def securityIssue(self):
        with tempfile.NamedTemporaryFile(delete=False,suffix='.py', mode='w+t') as temp_code:
            temp_code.write(self.raw_code)
        try:
            result = subprocess.run(
                ['bandit', temp_code.name],
                capture_output=True,
                text=True
            )
            if result.stdout:
                return result
        except:
            print("erm?")
        finally:
            os.remove(temp_code.name)



        
        


    
