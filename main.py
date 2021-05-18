class GPU:
    def __init__(self, frequency, memory, model, currTemperature, maxTemperature):
        self.frequency = frequency
        self.memory = memory
        self.model = model
        self.currTemperature = currTemperature
        self.maxTemperature = maxTemperature


class CPU:
    def __init__(self, frequency, socket, model, currTemperature, maxTemperature):
        self.frequency = frequency
        self.socket = socket
        self.model = model
        self.currTemperature = currTemperature
        self.maxTemperature = maxTemperature


class RAM:
    def __init__(self, memory, frequency):
        self.memory = memory
        self.frequency = frequency


class Motherboard:
    def __init__(self, socket):
        self.socket = socket


class GraphicsReproductionSystem:
    def __init__(self, GPU, CPU, RAM, Motherboard):
        self.gpu = GPU
        self.cpu = CPU
        self.ram = RAM
        self.mother = Motherboard

    def displayGraphics(self):
        print("Graphical interface has been displayed")


class Cooler:
    def __init__(self, frequency, isOn=False):
        self.frequency = frequency
        self.isOn = isOn

    def setFrequency(self, frequency):
        self.frequency = frequency


class HeatPipe:
    def __init__(self, heatDissipation):
        self.heatDissipation = heatDissipation


class CoolingSystem:
    def __init__(self, Cooler, HeatPipe):
        self.cooler = Cooler
        self.heatPipe = HeatPipe


class Generator:
    def __init__(self, power):
        self.power = power


class PowerSupplySystem:
    def __init__(self, Generator):
        self.generator = Generator


class Button:
    def __init__(self, isOn=False):
        self.isOn = isOn


class Mouse:
    def __init__(self, name, isWireless):
        self.name = name
        self.isWireless = isWireless


class Keyboard:
    def __init__(self, name, hasNumLock):
        self.name = name
        self.hasNumLock = hasNumLock


class InputSystem:
    def __init__(self, Mouse, Keyboard):
        self.mouse = Mouse
        self.keyboard = Keyboard


class Monitor:
    def __init__(self, inch, frequency):
        self.inch = inch
        self.frequency = frequency


class Headphones:
    def __init__(self, decibels, decRange, pluggedIn, connector="miniJack 3.5"):
        self.decibels = decibels
        self.decRange = decRange
        self.pluggedIn = pluggedIn
        self.connector = connector


class Columns:
    def __init__(self, decibels, decRange, pluggedIn):
        self.decibels = decibels
        self.decRange = decRange
        self.pluggedIn = pluggedIn


class Audio:
    def __init__(self, Headphones, Columns):
        self.headphones = Headphones
        self.columns = Columns


class OutputSystem:
    def __init__(self, Monitor, Audio):
        self.monitor = Monitor
        self.audio = Audio


class ControlSystem:
    def __init__(self, InputSystem, OutputSystem):
        self.inp = InputSystem
        self.out = OutputSystem


class OS:
    def __init__(self, isOn=False):
        self.isOn = isOn

    def turnOnOffCooler(self, coolingS):
        coolingS.cooler.isOn = True if not coolingS.cooler.isOn else False
        print("Cooler has been turned on") if coolingS.cooler.isOn else print("Cooler has been turned off")

    def turnOn(self, comp, name):
        if comp.grs.gpu.currTemperature >= comp.grs.gpu.maxTemperature or comp.grs.cpu.currTemperature >= comp.grs.cpu.maxTemperature:
            comp.os.turnOnOffCooler(comp.coolingS)
        comp.grs.displayGraphics()
        print("Hello, {}!".format(name))

    def playSound(self, controlS):
        if not (controlS.out.audio.columns.pluggedIn or controlS.out.audio.headphones.pluggedIn):
            print("No audio device was found")
        else:
            print("Audio playback through headphones") if controlS.out.audio.headphones.pluggedIn else print("Audio playback through columns")

    def changeVolume(self, controlS, lowOrIncrease):
        if not (controlS.out.audio.columns.pluggedIn or controlS.out.audio.headphones.pluggedIn):
            print("No audio device was found")
        else:
            if controlS.out.audio.headphones.pluggedIn:
                if lowOrIncrease == "+":
                    if controlS.out.audio.headphones.decibels < controlS.out.audio.headphones.decRange[1]:
                        controlS.out.audio.headphones.decibels += 1
                    else:
                        print("Such volume is not supported by device")
                    print("Current volume: {}".format(controlS.out.audio.headphones.decibels))
                elif lowOrIncrease == "-":
                    if controlS.out.audio.headphones.decibels > controlS.out.audio.headphones.decRange[0]:
                        controlS.out.audio.headphones.decibels -= 1
                    else:
                        print("Such volume is not supported by device")
                    print("Current volume: {}".format(controlS.out.audio.headphones.decibels))
                else:
                    print("Enter + for increase volume and - for low")
            else:
                if lowOrIncrease == "+":
                    if controlS.out.audio.columns.decibels < controlS.out.audio.columns.decRange[1]:
                        controlS.out.audio.columns.decibels += 1
                    else:
                        print("Such volume is not supported by device")
                    print("Current volume: {}".format(controlS.out.audio.columns.decibels))
                elif lowOrIncrease == "-":
                    if controlS.out.audio.columns.decibels > controlS.out.audio.columns.decRange[0]:
                        controlS.out.audio.columns.decibels -= 1
                    else:
                        print("Such volume is not supported by device")
                    print("Current volume: {}".format(controlS.out.audio.columns.decibels))
                else:
                    print("Enter + for increase volume and - for low")

    def generateInfo(self, grs, controlS, coolingS):
        f = open("info.txt", "w")
        f.write("GPU model: {}, frequency: {} Ghz, memory: {} Gb\n".format(grs.gpu.model, grs.gpu.frequency, grs.gpu.memory))
        f.close()
        f = open("info.txt", "a")
        f.write("CPU model: {}, frequency: {} Ghz, socket: {}\n".format(grs.cpu.model, grs.cpu.frequency, grs.cpu.socket))
        f.write("RAM memory: {} Gb, frequency: {} Ghz\n".format(grs.ram.memory, grs.ram.frequency))
        f.write("Motherboard socket: {}\n".format(grs.mother.socket))
        f.write("Mouse name: {}, is wireless: {}\n".format(controlS.inp.mouse.name, controlS.inp.mouse.isWireless))
        f.write("Keyboard name: {}, has NumLock: {}\n".format(controlS.inp.keyboard.name, controlS.inp.keyboard.hasNumLock))
        f.write("Monitor diagonal: {} inch, frequency: {}\n".format(controlS.out.monitor.inch, controlS.out.monitor.frequency))
        f.write("Cooler frequency: {}\n".format(coolingS.cooler.frequency))
        f.write("Heat dissipation: {}\n".format(coolingS.heatPipe.heatDissipation))
        f.close()
        print("File with info has been generated")

    def setMaxTemperature(self, grs, target, newMaxTemp):
        if target == "GPU":
            grs.gpu.maxTemperature = newMaxTemp
            print("New maximum allowed temperature for GPU is {}".format(grs.gpu.maxTemperature))
            print("Current temperature is: {}".format(grs.gpu.currTemperature))
        elif target == "CPU":
            grs.cpu.maxTemperature = newMaxTemp
            print("New maximum allowed temperature for CPU is {}".format(grs.cpu.maxTemperature))
            print("Current temperature is: {}".format(grs.cpu.currTemperature))
        else:
            print("Enter CPU or GPU to change new maximum permitted temperature")


class Windows(OS):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def turnOnOffCooler(self, coolingS):
        super().turnOnOffCooler(coolingS)

    def turnOn(self, comp, name):
        super().turnOn(comp, name)

    def playSound(self, controlS):
        super().playSound(controlS)

    def changeVolume(self, controlS, lowOrIncrease):
        super().changeVolume(controlS, lowOrIncrease)

    def generateInfo(self, grs, controlS, coolingS):
        super().generateInfo(grs, controlS, coolingS)

    def setMaxTemperature(self, grs, target, newMaxTemp):
        super().setMaxTemperature(grs, target, newMaxTemp)


class Linux(OS):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def turnOnOffCooler(self, coolingS):
        super().turnOnOffCooler(coolingS)

    def turnOn(self, comp, name):
        super().turnOn(comp, name)

    def playSound(self, controlS):
        super().playSound(controlS)

    def changeVolume(self, controlS, lowOrIncrease):
        super().changeVolume(controlS, lowOrIncrease)

    def generateInfo(self, grs, controlS, coolingS):
        super().generateInfo(grs, controlS, coolingS)

    def setMaxTemperature(self, grs, target, newMaxTemp):
        super().setMaxTemperature(grs, target, newMaxTemp)


class Computer:
    def __init__(self, Button, OS, Windows, Linux, PowerSupplySystem, GraphicReproductionSystem, ControlSystem, CoolingSystem):
        self.btn = Button
        self.os = OS
        self.windows = Windows
        self.linux = Linux
        self.pss = PowerSupplySystem
        self.grs = GraphicReproductionSystem
        self.controlS = ControlSystem
        self.coolingS = CoolingSystem

    def chooseOs(self, osName):
        self.os = self.linux if osName == "Linux" else self.windows


class User:
    def __init__(self, name):
        self.name = name

    def turnOnOff(self, comp, name, osName):
        if comp.pss.generator.power != 220:
            print("Unsuitable voltage")
        else:
            comp.btn.isOn = True if not comp.btn.isOn else False
            if comp.btn.isOn:
                comp.chooseOs(osName)
                comp.os.turnOn(comp, name)
            else:
                comp.os.isOn = False
                comp.coolingS.cooler.isOn = False
                print("Cooling system has been turned off")
                print("Googbye, {}".format(name))
                print("Shutdown")

    def changeMaxTemperature(self, comp, target, newMaxTemp):
        comp.os.setMaxTemperature(comp.grs, target, newMaxTemp)
        if comp.grs.gpu.maxTemperature >= comp.grs.gpu.currTemperature:
            comp.coolingS.cooler.isOn = True
            print("Cooler has been turned on")
        if comp.grs.cpu.maxTemperature >= comp.grs.cpu.currTemperature:
            comp.coolingS.cooler.isOn = True
            print("Cooler has been turned on")

    def listenToMusic(self, comp):
        comp.os.playSound(comp.controlS)

    def changeVolume(self, comp, lowOrIncrease):
        comp.os.changeVolume(comp.controlS, lowOrIncrease)

    def getInfo(self, comp):
        comp.os.generateInfo(comp.grs, comp.controlS, comp.coolingS)

    def plugHeadphonesInOut(self, comp):
        comp.controlS.out.audio.headphones.pluggedIn = True if not comp.controlS.out.audio.headphones.pluggedIn else False
        if comp.controlS.out.audio.headphones.pluggedIn:
            print("Headphones have been plugged in")
        else:
            print("Headphones have been plugged out")


def main():
    gpu = GPU(1.5, 6, "NVIDIA GeForse GTX 1660 Ti", 30, 55)
    cpu = CPU(2, "BGA-1526", "Intel Core i5 Ice Lake", 25, 50)
    ram = RAM(16, 3.4)
    mother = Motherboard("Socket H2")
    grs = GraphicsReproductionSystem(gpu, cpu, ram, mother)
    cooler = Cooler(1400)
    heatPipe = HeatPipe(10**7)
    coolingS = CoolingSystem(cooler, heatPipe)
    generator = Generator(220)
    pss = PowerSupplySystem(generator)
    btn = Button()
    mouse = Mouse("Razer Naga Pro", True)
    keyboard = Keyboard("HyperX Alloy Origins", True)
    inp = InputSystem(mouse, keyboard)
    monitor = Monitor(22, 144)
    headphones = Headphones(75, [60, 95], False)
    columns = Columns(99, [50, 100], True)
    audio = Audio(headphones, columns)
    out = OutputSystem(monitor, audio)
    controlS = ControlSystem(inp, out)
    windows = Windows("Windows 10")
    linux = Linux("Ubuntu 21.04")
    os = windows
    computer = Computer(btn, os, windows, linux, pss, grs, controlS, coolingS)
    name = input("Enter your username: ")
    user = User(name)
    choseOs = input("Enter os name (default os is Windows): ")
    user.turnOnOff(computer, user.name, choseOs)
    option = 0
    while True:
        print("1 - Change maximum temperature")
        print("2 - Listen to music")
        print("3 - Change volume")
        print("4 - Plug headphones in or out")
        print("5 - Get info about your computer")
        print("6 - Turn computer off")
        option = input("Choose option to do: ")
        if option == "1":
            target = input("Enter device you want to change temperature on: ")
            newTemp = input("Enter new value for maximum temperature (only digits): ")
            if not newTemp.isdigit():
                print("Incorrect value for temperature")
            else:
                user.changeMaxTemperature(computer, target, int(newTemp))
        if option == "2":
            user.listenToMusic(computer)
        if option == "3":
            lowOrIncrease = input("Enter + for low and - for increase volume: ")
            user.changeVolume(computer, lowOrIncrease)
        if option == "4":
            user.plugHeadphonesInOut(computer)
        if option == "5":
            user.getInfo(computer)
        if option == "6":
            user.turnOnOff(computer, user.name, computer.os.name)
            break
        else:
            print("Please choose one of the options")


if __name__ == "__main__":
    main()

