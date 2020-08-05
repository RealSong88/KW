class Math:
    def __init__(self, source):
        self.sum_list = []
        self.source = source
        self.chk_sump()

    def chk_sump(self):
        for i in self.source:
            chk_dupl = False
            no_dupl = None
            for j in range(len(self.sum_list)):
                if i[0] == self.sum_list[j][0]:
                    chk_dupl = True
                    no_dupl = j

            if chk_dupl:
                self.sum_list[no_dupl][1] += i[1]
            else:
                self.sum_list.append(i)


