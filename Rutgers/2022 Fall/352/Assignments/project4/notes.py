import time
# send packets

# wait for ACKs
ACKs = {}
RTOs = {}
for seqNo in []:
    ACKs[seqNo] = time.time()

while True:
    value = None
    if value and value.ack:
        ACKs[value.ack] = 0
    for (ackNum, t) in ACKs:
        if time.time() - t > 0.5:
            RTOs[ackNum] = True
            # we know this has timed out
    if any(RTOs.values()):
        break
# retransmit