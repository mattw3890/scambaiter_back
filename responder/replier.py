import os.path
import random
import re
from abc import ABC, abstractmethod

#from text_utils.text_filter import *
from .Chatgpt_Replier import gen_text1, gen_text2, gen_text3, gen_text_fake
# from .gen import gen_text
from .classifier import classify
from secret import MAIL_ARCHIVE_DIR, TEMPLATES_DIR # NEO_ENRON_PATH, NEO_RAW_PATH,

#text_filters = [
 #   RemoveSymbolLineTextFilter(),
   # RemoveInfoLineTextFilter(),
 #   RemoveSensitiveInfoTextFilter(),
 #   RemoveSpecialPunctuationTextFilter(),
#   RemoveStrangeWord(),
 #   MultiSymbolIntegrationTextFilter(),
#]


class Replier(ABC):
    name = "AbstractReplier"

    @abstractmethod
    def _gen_text(self, prompt, higherTemp) -> str:
        print(f"Generating reply using {self.name}")
        return prompt

    def get_reply(self, content, higherTemp):
        #for text_filter in text_filters:
         #   content = text_filter.filter(content)

        res = self._gen_text(content, higherTemp)

        if "[bait_end]" in res:
            res = res.split("[bait_end]", 1)[0]

        m = re.match(r"^.*[.?!]", res, re.DOTALL)
        if m:
            res = m.group(0)

        return res

    def get_reply_by_his(self, addr, higherTemp):
        with open(os.path.join(MAIL_ARCHIVE_DIR, addr + ".his"), "r", encoding="utf8") as f:
            content = f.read()
        return self.get_reply(content + "\n[bait_start]\n", higherTemp)


# class NeoEnronReplier(Replier):
#     name = "NeoEnron"
#
#     def _gen_text(self, prompt) -> str:
#         print(f"Generating reply using {self.name}")
#         return gen_text(NEO_ENRON_PATH, prompt)
#
#
# class NeoRawReplier(Replier):
#     name = "NeoRaw"
#
#     def _gen_text(self, prompt) -> str:
#         print(f"Generating reply using {self.name}")
#         return gen_text(NEO_RAW_PATH, prompt)
#

class ClassifierReplier(Replier):
    name = "Classifier"

    def _gen_text(self, prompt, higherTemp):
        scam_type = classify(prompt)
        template_dir = os.path.join(TEMPLATES_DIR, scam_type)
        target_filename = random.choice(os.listdir(template_dir))

        with open(os.path.join(template_dir, target_filename), "r", encoding="utf8") as f:
            res = f.read()

        return res + "[bait_end]"


class TemplateReplier(Replier):
    name = "Template"

    def _gen_text(self, prompt, higherTemp) -> str:
        template_dir = os.path.join(TEMPLATES_DIR, random.choice(os.listdir(TEMPLATES_DIR)))
        target_filename = random.choice(os.listdir(template_dir))

        with open(os.path.join(template_dir, target_filename), "r", encoding="utf8") as f:
            res = f.read()

        return res + "[bait_end]"

class ChatReplier1(Replier):
    name = "Chat1"

    def _gen_text(self,prompt,higherTemp) -> str:
        print(f"Generating reply using {self.name}")
        res = gen_text1(prompt, higherTemp)
        return res + "[bait_end]"



class ChatReplier2(Replier):
    name = "Chat2"

    def _gen_text(self,prompt,higherTemp) -> str:
        print(f"Generating reply using {self.name}")
        res = gen_text2(prompt)
        return res + "[bait_end]"
    

class ChatReplier3(Replier):
    name = "Chat3"   
    def _gen_text(self, prompt, higherTemp) -> str:
            print(f"Generating reply using {self.name}")
            res = gen_text3(prompt, higherTemp)
            return res + "[bait_end]"

class FakeInfoResponse(Replier):
    name = "Fake1"   
    def _gen_text(self, prompt, higherTemp) -> str:
            print(f"Generating reply using {self.name}")
            res = gen_text_fake(prompt, higherTemp)
            return res + "[bait_end]"
