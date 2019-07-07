import logging
import socket
import sys
import time
import pigpio
import smbus

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

class CarManager(object):
  
  def __init__(self, servo=4):
        self.response = None
        self.pi = pigpio.pi()
        self.servo = servo
        self.bus = smbus.SMBus(1)
        self.address = 0x04

  def send_command(self, command):
      logger.info({'action': 'send_command', 'command': command})
      code = ''
      if command=='forward':
        pwm = 900
        code='f'
      elif command=='back':
        pwm = 1300
        code='b'
      elif command=='right':
        pwm = 1700
        code='r'
      elif command=='left':
        pwm = 2100
        code='l'
      
      self.pi.set_servo_pulsewidth(self.servo, pwm)
      self.bus.write_byte(self.address, ord(code))
      time.sleep(3)

      return self.response

  def forward(self):
      return self.send_command('forward')

  def back(self):
      return self.send_command('back')

  def left(self):
      return self.send_command('left')

  def right(self):
      return self.send_command('right')
