# Mixin JsonMixin с метод to_json(),
# използвайки getattr() за динамично извличане на данни

import json

class JsonMixin:
    def to_json(self):
        current_data = getattr(self, "data", {})
        return json.dumps(current_data)

