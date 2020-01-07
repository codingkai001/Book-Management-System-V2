activate_this = r'E:\Book-Management-System-V2\env\bin\activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
from app import create_app


sys.path.insert(0, r"E:\Book-Management-System-V2")

application = create_app()
