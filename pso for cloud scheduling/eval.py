from Workflow import Workflow
from PSO import PSO

workflowPath = "./Montage_25.xml"
wf = Workflow(workflowPath)
wf.setDeadline(11457)
tmpc = 0
for i in range(5):
    ps = PSO(500)
    tmpc += ps.schedule(wf)

print("ave :  " + str(tmpc/5))
