
if "take drug" in result_of_talk_array[0]:
    from orders import *

    final_text = result_of_talk_array[0].split()
    final_text.remove("take")
    final_text.remove("drug")
    jeckvoice("ok doctor thanks i will take {} and tell you what habbened".format(final_text[0]))
    take_drug(name_drug=final_text[0])