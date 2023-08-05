class ModuleReloader:
    def btn_click(self,detail):
        contet = f"from {self.dic[detail.description]} import {detail.description}\n"
        contet += "from ModuleDB import ModuleDB\n"
        contet += f"ModuleDB.reloadClass({detail.description})"
        exec(contet)
        self._swwov._click_display_region.display(ModuleDB.colorPrint("python", contet), ipy=False, clear=True)
    def main(self):
        self.dic = SerializationDB.readPickle(LibsDB.picklePath("fromFileImportClass"))
        ds = DicSearch(self.dic)
        se = SearchEngine()
        se.default_display(False)
        bvwp =ButtonViewWithPagination()
        bvwp.set_btn_click_func(self.btn_click)
        se.set_engine(ds)
        se.set_result_maker(bvwp)
        self._swwov = SearchWidgetWithOutputVisible()
        self._swwov.set_database(se)
        lay =self._swwov._make_layout()
        self._swwov.set_up()
        return lay