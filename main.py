from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from translator import translate_code

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def malayalam_print(value):
    translations = {
        True: "സത്യം",
        False: "അസത്യം",
        None: "ഒന്നുമില്ല"
    }
    return str(translations.get(value, value))


class CodeRequest(BaseModel):
    code: str


@app.post("/run")
def run_code(data: CodeRequest):

    python_code = translate_code(data.code)

    output = []

    def capture_print(value):
        output.append(
            malayalam_print(value)
        )

    exec_globals = {
        "malayalam_print": capture_print
    }

    exec(python_code, exec_globals)

    return {
        "python_code": python_code,
        "output": "\n".join(output)
    }