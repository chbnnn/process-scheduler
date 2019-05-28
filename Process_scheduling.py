import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from myui import *
import numpy as np
import time

# from collections import namedtuple
# Process = namedtuple('Process', ['PID', 'status', 'priority', 'need_time', 'remaining_time'])

class Process:
    def __init__(self, PID, status, priority, need_time, remaining_time):
        self.PID = PID
        self.status = status
        self.priority = priority
        self.need_time = need_time
        self.remaining_time = remaining_time


class PSWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class ProcessScheduling:
    def __init__(self):
        self.p_max = 10
        self.scheduling_method = 'round_robin'

        self.ready_queue = []
        self.finished_queue = []
        self.count = 0

        self.gui = PSWindow()
        self.gui.setWindowTitle('单处理器调度模拟器')
        self._generate_one_process()
        self._generate_one_process()
        self._generate_one_process()

        self.refresh_running_table()


    def start_scheduling(self):
        method_dict = {'时间片轮转': 'round_robin',
                       '优先级': 'priority',
                       '最短进程优先': 'shortest_process_next',
                       '最短剩余时间': 'shortest_remaining_time'}

        print(self.gui.btn_method.currentText())
        self.scheduling_method = method_dict[self.gui.btn_method.currentText()]
        print('scheduling start')
        print(self.scheduling_method)

        if self.scheduling_method == 'round_robin':
            self._round_robin_scheduling()
        elif self.scheduling_method == 'priority':
            self._priority_scheduling()
        elif self.scheduling_method == 'shortest_process_next':
            self._shortest_process_next_scheduling()
        elif self.scheduling_method == 'shortest_remaining_time':
            self._shortest_remaining_time_scheduling()

    def _check_process_num(self):
        if len(self.ready_queue) != 0:
            return
        if self.count < 10:
            self._generate_one_process()

    def _generate_one_process(self):
        priority = np.random.randint(1, 11)
        need_time = np.random.randint(1, 11)
        p = Process(self.count, 'ready', priority, need_time, need_time)
        self.count += 1
        self.ready_queue.append(p)

    def _round_robin_scheduling(self):
        while True:
            self.refresh_table()
            if len(self.ready_queue) == 0 and self.count > 10:
                break
            elif len(self.ready_queue) == 0:
                self._check_process_num()

            p = self.ready_queue.pop(0)
            if p.remaining_time == 1:
                p.remaining_time = 0
                p.status = 'finished'
                self.finished_queue.append(p)
            else:
                p.remaining_time -= 1
                self.ready_queue.append(p)

            self._refresh_process_pool()

        print('scheduling done')

    def _priority_key(self, process):
        return process.priority

    def _priority_scheduling(self):
        while True:
            self.refresh_table()
            if len(self.ready_queue) == 0 and self.count > 10:
                break
            elif len(self.ready_queue) == 0:
                self._check_process_num()

            self.ready_queue = sorted(self.ready_queue, key=self._priority_key, reverse=True)

            p = self.ready_queue.pop(0)
            if p.remaining_time == 1:
                p.remaining_time = 0
                p.status = 'finished'
                self.finished_queue.append(p)
            else:
                p.remaining_time -= 1
                p.priority -= 1
                self.ready_queue.append(p)

            self._refresh_process_pool()

    def _time_need_key(self, process):
        return process.remaining_time

    def _shortest_process_next_scheduling(self):
        self.ready_queue = sorted(self.ready_queue, key=self._time_need_key)
        while True:
            self.refresh_table()
            if len(self.ready_queue) == 0 and self.count > 10:
                break
            elif len(self.ready_queue) == 0:
                self._check_process_num()

            p = self.ready_queue[0]
            p.remaining_time -= 1
            if p.remaining_time == 0:
                p = self.ready_queue.pop(0)
                p.status = 'finished'
                self.finished_queue.append(p)
                self.ready_queue = sorted(self.ready_queue, key=self._time_need_key)

            self._refresh_process_pool()

    def _time_remain_key(self, process):
        return process.remaining_time

    def _shortest_remaining_time_scheduling(self):
        while True:
            self.refresh_table()
            if len(self.ready_queue) == 0 and self.count > 10:
                break
            elif len(self.ready_queue) == 0:
                self._check_process_num()

            self.ready_queue = sorted(self.ready_queue, key=self._time_remain_key)

            p = self.ready_queue.pop(0)
            if p.remaining_time == 1:
                p.remaining_time = 0
                p.status = 'finished'
                self.finished_queue.append(p)
            else:
                p.remaining_time -= 1
                self.ready_queue.append(p)

            self._refresh_process_pool()

    def _refresh_process_pool(self):
        if self.count > self.p_max:
            return
        probability = np.random.randint(0, 2)
        if probability == 1:
            self._generate_one_process()

    def clear_table(self, table):
        for i in range(10):
            table.setItem(i, 0, QTableWidgetItem(''))
            table.setItem(i, 1, QTableWidgetItem(''))
            table.setItem(i, 2, QTableWidgetItem(''))
            table.setItem(i, 3, QTableWidgetItem(''))
            table.setItem(i, 4, QTableWidgetItem(''))

    def refresh_table(self):
        self.refresh_running_table()
        self.refresh_finished_table()

    def refresh_running_table(self):
        time.sleep(0.05)
        self.clear_table(self.gui.running_table)

        for i in range(len(self.ready_queue)):
            PID = QTableWidgetItem(str(self.ready_queue[i].PID))
            status = QTableWidgetItem(self.ready_queue[i].status)
            priority = QTableWidgetItem(str(self.ready_queue[i].priority))
            need_time = QTableWidgetItem(str(self.ready_queue[i].need_time))
            remaining_time = QTableWidgetItem(str(self.ready_queue[i].remaining_time))

            self.gui.running_table.setItem(i, 0, PID)
            self.gui.running_table.setItem(i, 1, status)
            self.gui.running_table.setItem(i, 2, priority)
            self.gui.running_table.setItem(i, 3, need_time)
            self.gui.running_table.setItem(i, 4, remaining_time)
        QApplication.processEvents()
        time.sleep(0.05)

    def refresh_finished_table(self):
        time.sleep(0.05)
        self.clear_table(self.gui.finished_table)
        for i in range(len(self.finished_queue)):
            PID = QTableWidgetItem(str(self.finished_queue[i].PID))
            status = QTableWidgetItem(self.finished_queue[i].status)
            priority = QTableWidgetItem(str(self.finished_queue[i].priority))
            need_time = QTableWidgetItem(str(self.finished_queue[i].need_time))
            remaining_time = QTableWidgetItem(str(self.finished_queue[i].remaining_time))

            self.gui.finished_table.setItem(i, 0, PID)
            self.gui.finished_table.setItem(i, 1, status)
            self.gui.finished_table.setItem(i, 2, priority)
            self.gui.finished_table.setItem(i, 3, need_time)
            self.gui.finished_table.setItem(i, 4, remaining_time)
        QApplication.processEvents()
        time.sleep(0.05)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    method_dict = {'时间片轮转': 'round_robin',
                   '优先级': 'priority',
                   '最短进程优先': 'shortest_process_next',
                   '最短剩余时间': 'shortest_remaining_time'}

    ps = ProcessScheduling()

    ps.gui.btn_start.clicked.connect(ps.start_scheduling)

    ps.gui.show()
    sys.exit(app.exec())