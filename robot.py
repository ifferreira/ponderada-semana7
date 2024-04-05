import pydobot

class InteliArm(pydobot.Dobot):
    def __init__(self, port=None, verbose=False):
        super().__init__(port=port, verbose=verbose)
    def movej_to(self, x, y, z, r, wait=False):
        self._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVJ_XYZ, wait=wait)
    def movel_to(self, x, y, z, r, wait=False):
        self._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVL_XYZ, wait=wait)

braco_robotico = InteliArm(port='COM6', verbose=False)

def definir_posicao(positionX, positionY, positionZ):
    braco_robotico.movej_to(positionX, positionY, positionZ, 0, wait=True)


