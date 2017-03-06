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
    p.include('distributed_cnot.quil')
    cnot30 = Program("DISTRIBUTED_CNOT 3 0 2 1 [2] [1]")
    print p + cnot30
    cxn = qvm.Connection()
    print cxn.run_and_measure(p + cnot30, [3,0], 1)
    print cxn.run_and_measure(p + Program(X(0)) + cnot30, [3,0], 1)
    print cxn.run_and_measure(p + Program(X(3)) + cnot30, [3,0], 1)
    print cxn.run_and_measure(p + Program(X(3),X(0)) + cnot30, [3,0], 1)
