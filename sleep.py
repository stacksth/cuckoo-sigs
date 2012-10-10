# Copyright (C) 2012 Thomas "stacks" Birn (@stacksth)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature

class LongSleep(Signature):
    name = "longsleep"
    description = "Contains a long sleep > 5min"
    severity = 2
    categories = ["anti-debug"]
    authors = ["Thomas Birn"]
    minimum = "0.4.2"

    def run(self, results):
        for process in results["behavior"]["processes"]:
            for call in process["calls"]:
                if call["api"].startswith("NtDelayExecution"):
                    for argument in call["arguments"]:
                        if argument["name"] == "Milliseconds" and int(argument["value"]) > 300000:
                            return True

        return False