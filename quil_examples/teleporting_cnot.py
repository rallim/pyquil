##############################################################################
# Copyright 2016-2017 Rigetti Computing
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
##############################################################################

from pyquil.quil import Program
import pyquil.forest as qvm
from pyquil.gates import X


if __name__ == '__main__':
    p = Program()
    p.include('xor.quil')
    p.include('teleporting_cnot.quil')
    # compute CNOT 5 0 via teleporting_cnot to 3 2 
    cnot50_32 = Program("TELEPORTING_CNOT 5 0 3 2 4 1 [0] [1] [5] [4] [2]")
    print p + cnot50_32
    cxn = qvm.Connection()
    print cxn.run_and_measure(p + cnot50_32, [3,2], 1)
    print cxn.run_and_measure(p + Program(X(0)) + cnot50_32, [3,2], 1)
    print cxn.run_and_measure(p + Program(X(5)) + cnot50_32, [3,2], 1)
    print cxn.run_and_measure(p + Program(X(5),X(0)) + cnot50_32, [3,2], 1)
