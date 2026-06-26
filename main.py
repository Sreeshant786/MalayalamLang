from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from keywords_malayalam import KEYWORDS as MALAYALAM_KEYWORDS
from keywords_latin import KEYWORDS as LATIN_KEYWORDS

from translator import translate_code



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

def convert_output(value, mode):

    if mode == "latin":

        translations = {
            True: "sathyam",
            False: "asathyam",
            None: "onnumilla"
        }

    else:

        translations = {
            True: "സത്യം",
            False: "അസത്യം",
            None: "ഒന്നുമില്ല"
        }

    return str(
        translations.get(
            value,
            value
        )
    )


class CodeRequest(BaseModel):
    code: str
    mode: str


@app.post("/run")
def run_code(data: CodeRequest):

    # Select keyword dictionary
    if data.mode == "latin":
        keywords = LATIN_KEYWORDS
    else:
        keywords = MALAYALAM_KEYWORDS

    # Translate MalayalamLang / Roman Malayalam
    # into Python
    python_code = translate_code(
        data.code,
        keywords
    )

    output = []

    def capture_print(value):

        output.append(
            convert_output(
                value,
                data.mode
            )
        )

    exec_globals = {
        "malayalam_print": capture_print
    }

    exec(
        python_code,
        exec_globals
    )

    return {
        "python_code": python_code,
        "output": "\n".join(output)
    }