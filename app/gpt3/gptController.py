from typing import List, Dict, Any
from openai import Configuration, OpenAIApi
import os
from dotenv import load_dotenv
load_dotenv('./.env')

# EXAMPLE TO CALL AND USE THE UTILS
# from gpt_controller import extractor
# result = extractor(text, directive, format=True)
# =================================

class GPTController:
    @staticmethod
    async def extractor(req: dict, res: dict, next: callable) -> None:
        text = req.get('text')
        directive = req.get('directive')
        format = req.get('format')

        if len(text) < 3:
            res['status'] = 'fail'
            res['errors'] = ['CP Problem text is required']
            return

        if len(directive) < 1:
            res['status'] = 'fail'
            res['errors'] = ['Directive is required']
            return

        try:
            configuration = Configuration(
                api_key=os.getenv("OPENAI_API_KEY")
            )
            openai = OpenAIApi(configuration)

            prompt = f"{directive}. Apply on this text: {text}. "
            if format:
                prompt += f"The response must be encoded on this way: {encoding}"
            response = await openai.create_completion(
                model=os.getenv("OPENAI_MODEL"),
                prompt=prompt,
                temperature=os.getenv("OPENAI_TEMPERATURE"),
                max_tokens=os.getenv("OPENAI_MAX_TOKEN"),
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            api_result = parse_string(response['choices'][0]['text'])

            res['status'] = 'success'
            res['data'] = {
                'id': response['id'],
                'model': response['model'],
                'result': api_result,
                'usage': response['usage']
            }

        except Exception as e:
            res['status'] = 'fail'
            res['errors'] = [str(e)]

        return
