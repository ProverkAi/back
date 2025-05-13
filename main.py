from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json

from schemas import CheckRequest, CheckResponse
from configs.ai import client, promt, task_response_schema

app = FastAPI()


@app.post("/check", response_model=CheckResponse)
async def check_solution(data: CheckRequest):
    try:
        content = json.dumps({
            "task": data.user_task,
            "solution": data.user_solution
        })

        completion = client.chat.completions.create(
            model="qwen2.5-coder-14b-instruct",
            messages=[
                {"role": "system", "content": promt},
                {"role": "user", "content": content}
            ],
            response_format=task_response_schema,
            temperature=0.3,
            max_tokens=500,
            top_p=0.7
        )

        return {"result": completion}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
