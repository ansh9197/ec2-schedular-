import boto3
import schedule
import time
from datetime import datetime
import threading
from whatsapp_notifier import send_whatsapp

ec2 = boto3.client('ec2', region_name='us-east-2')


def list_instances():
    return [
        {"id": "i-032257e1cd39d61a4", "type": "t2.micro", "state": "running", "launch_time": "now"}   #put ec2 id 
    ]
            
    return instances

def start_instance(instance_id):
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        msg = f"✅ EC2 instance {instance_id} started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        send_whatsapp(msg)
    except Exception as e:
        send_whatsapp(f"❌ EC2 Start Failed: {instance_id} - {e}")

def stop_instance(instance_id):
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        msg = f"🛑 EC2 instance {instance_id} stopped at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        send_whatsapp(msg)
    except Exception as e:
        send_whatsapp(f"❌ EC2 Stop Failed: {instance_id} - {e}")

def schedule_start(instance_id, start_time):
    schedule.every().day.at(start_time).do(start_instance, instance_id=instance_id)

def schedule_stop(instance_id, stop_time):
    schedule.every().day.at(stop_time).do(stop_instance, instance_id=instance_id)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)