
import time
import sys
import os
from bioblend.galaxy import GalaxyInstance

api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
gi = GalaxyInstance(url="https://usegalaxy.org", key=api_key)
history_id = "bbd44e69cb8906b5aea3847d2c8aabd9"
genome_id = "f9cad7b01a472135ab799b882afc5f31"
gtf_id = "f9cad7b01a472135534c5697946e5dfb"
variant_calling_wf_id = "5b6330a27ca61ba8"

res_inv_id = "26e57b476cc2dbee"
sus_inv_id = "75a6b66be3601c20"

def wait_and_launch(inv_id, label):
    print(f"Monitoring {label} invocation {inv_id}...")
    while True:
        try:
            inv = gi.invocations.show_invocation(inv_id)
            if inv['state'] == 'scheduled':
                # Check if all jobs in invocation are done
                steps = inv.get('steps', [])
                if steps and all(gi.jobs.show_job(s['job_id'])['state'] == 'ok' for s in steps if s.get('job_id')):
                    out_colls = inv.get('output_collections', {})
                    if out_colls:
                        coll = list(out_colls.values())[0]
                        print(f"{label} download complete. Launching variant calling...")
                        gi.workflows.invoke_workflow(
                            variant_calling_wf_id,
                            inputs={
                                '0': {'id': coll['id'], 'src': 'hdca'},
                                '1': {'id': gtf_id, 'src': 'hda'},
                                '2': {'id': genome_id, 'src': 'hda'}
                            },
                            history_id=history_id
                        )
                        return
            elif inv['state'] in ['cancelled', 'failed']:
                print(f"{label} invocation failed.")
                return
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(60)

# Run both in sequence or use threading/subprocess if needed, 
# but simple sequential check for completion is fine for this task.
wait_and_launch(res_inv_id, "Resistant")
wait_and_launch(sus_inv_id, "Susceptible")
