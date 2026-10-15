from maps.AbstractGakushoku import AbstractGakushoku
class GakushokuSample(AbstractGakushoku):
    def get_menu(self):
        return "おにぎり"
    
    def get_summary(self):
        return "安い"
    
    def get_author(self):
        return "小酒井友紀"