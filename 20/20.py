import re
import sys
import dataclasses
from typing import List
sys.setrecursionlimit(10000)


# with open("input_long.txt") as f:
with open("input.txt") as f:
    ls = f.readlines()

@dataclasses.dataclass
class Module:
    name: str
    output_modules: List[str]

    def process_pulse(self, m_name, pulse):
        pass

@dataclasses.dataclass
class Button(Module):
    def process_pulse(self, m_name, pulse):
        return pulse

@dataclasses.dataclass
class Broadcaster(Module):
    def process_pulse(self, m_name, pulse):
        return pulse

@dataclasses.dataclass
class FFModule(Module):
    on = False
    def process_pulse(self, m_name, pulse):
        if pulse == "H":
            pass
        elif pulse == "L":
            self.on = not self.on
            if self.on:
                return "H"
            return "L"
    def __repr__(self):
        return f"FFModule {self.name}: {self.on=}"

@dataclasses.dataclass
class ConjModule(Module):
    recent_pulse = None

    def init_input_modules(self, input_modules: List[str]):
        self.input_modules = input_modules
        self.recent_pulse = {}

        for m in input_modules:
            self.recent_pulse[m] = "L"

    def process_pulse(self, m_name, pulse):
        self.recent_pulse[m_name] = pulse
        if len(set(self.recent_pulse.values())) == 1 and list(self.recent_pulse.values())[0] == "H":
            return "L"
        return "H"

    def __repr__(self):
        return f"ConjModule {self.name}: {self.recent_pulse=}"

modules = {}

for l in ls:
    l = l.strip()
    m_name = l[:l.find("-")-1]
    out_mod_names = [m.strip() for m in l[l.find(">")+2:].split(",")]
    if "%" in m_name:
        m_name = m_name[1:]
        m = FFModule(m_name, out_mod_names)
    elif "&" in m_name:
        m_name = m_name[1:]
        m = ConjModule(m_name, out_mod_names)
    elif m_name == "broadcaster":
        m = Broadcaster(m_name, out_mod_names)

    modules[m_name] = m

conj_mods = [m for m in modules.values() if isinstance(m, ConjModule)]

for c_m in conj_mods:
    input_mods = []
    for m in modules.values():
        if c_m.name in m.output_modules:
            input_mods.append(m.name)
    c_m.init_input_modules(input_mods)


modules["button"] = Button("button", ["broadcaster"])

# print(modules)


high_pulses = 0
low_pulses = 0

# for i in range(113989708, 10000000000):
for i in range(1, 100):
    brk = False
    pulse_queue = [{"src": None, "dst": "button", "pulse": "L"}]
    while len(pulse_queue) > 0:
        q_elem = pulse_queue.pop(0)
        src = q_elem["src"]
        dst = q_elem["dst"]
        pulse = q_elem["pulse"]
        if dst == "rx" and pulse == "L":
            print(pulse_queue)
            brk = True
            break
        if dst not in modules:
            print(f"{pulse=}")
            continue
        ret_pulse = modules[dst].process_pulse(src, pulse)
        if not ret_pulse:
            continue
        for m_name in modules[dst].output_modules:
            if ret_pulse == "H":
                high_pulses += 1
            elif ret_pulse == "L":
                low_pulses += 1
            pulse_queue.append({"src": dst, "dst": m_name, "pulse": ret_pulse})
    if brk:
        break
    print("**************************")
    print(i)
    [print(f"{n}: {mod}") for n, mod in modules.items()]
    print("**************************")

print(i)

print(high_pulses)
print(low_pulses)

print(high_pulses*low_pulses)
