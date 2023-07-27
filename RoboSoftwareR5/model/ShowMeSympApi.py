from model.bloodFluidApi import *
from model.ConvulsionApi import *
from model.EyeContractApi import *
from model.EyeDiluteApi import * 
from model.HyperRespApi import *
from model.HypertenstionApi import *
from model.hyperthermiaApi import *
from model.HypoRespApi import *
from model.HypotensionApi import *
from model.WaterFluidApi import *
from model.DbContext import *
def F_ShowMeTheSym():
    NasalBloodFluidApi()
    MouthBloodFluidApi()
    F_SlowMoveApi()
    F_FastMoveApi()
    F_EyeContractApi()
    F_EyeDiluteApi()
    F_HyperBreath()
    HypertenstionMainApi()
    F_HyperThermia()
    F_HypoBreathApi()
    HypotenstionMainApi()
    F_MouthWaterFluidApi()
    F_NasalWaterFluidApi()



    

    return 0