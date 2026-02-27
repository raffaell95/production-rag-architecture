class OutputFormatter:

    @staticmethod
    def show(res: str):
        if "</think>" in res:
            res = res.split("</think>")[-1].strip()
        else:
            res = res.strip()

        print(res)