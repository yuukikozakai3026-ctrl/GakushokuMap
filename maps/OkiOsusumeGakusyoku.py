from maps.AbstractGakushoku import AbstractGakushoku

class okiOsusumeGakusyoku(AbstractGakushoku):
    def get_menu(self):
        return "温玉唐揚げ丼"
    
    def get_summary(self):
        return "美味しい"
    
    def get_author(self):
        return "木村"