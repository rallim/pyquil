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


if __name__ == '__main__':
    p = Program()
    p.include('margolus.quil')
    p.include('circuit_tester.quil')
    p.include('margolus_tests.quil')
    p.inst('MARGOLUS_TESTS 2 1 0')
    print p 
    cxn = qvm.Connection()
    addrs = range(24)
    addrs.reverse()
    print cxn.run(p, addrs, 1)
