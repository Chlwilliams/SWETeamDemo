import tempfile
import subprocess
import os

class CodeQuality():

    def __init__(self, raw_code):
        self.raw_code = raw_code

    def qualitycheck(self):
        with tempfile.NamedTemporaryFile(delete=False,suffix='.py', mode='w+t') as temp_code:
            temp_code.write(self.raw_code)

        errors = []
        try:
            result = subprocess.run(
                ['flake8', temp_code.name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if result.stdout:
                errors = result.stdout.splitlines()
        except Exception as e:
            errors.append(f"Error running flake8: {str(e)}")
        finally:
            os.remove(temp_code.name)
        ## Used Chatgpt For assistance on this section of the code
        return errors
        