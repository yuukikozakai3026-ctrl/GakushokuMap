from maps.AbstractGakushoku import AbstractGakushoku
class NimuraOsusume(AbstractGakushoku):
    def get_menu(self):
        return "カフェ&レスト セントラルのカレー"
    
    def get_summary(self):
        return "カツなど具材の量が多くて満足できる。福神漬けもついてくるし、盛り付けのサラダも美味しい。"
    
    def get_author(self):
        return "二村 将成"