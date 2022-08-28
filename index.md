# Hello, Linux

In this tutorial, you will learn some basic commands for nagivating the Linux filesystem and for working on remote Linux hosts. It should take you about 60-90 minutes to work through this tutorial.

Before you can run lab experiments on CloudLab, you will need to set up an account and join a project under the supervision of a research advisor or a course instructor. If you haven't set up your CloudLab account yet, follow the instructions in [Hello, CloudLab](https://teaching-on-testbeds.github.io/hello-cloudlab/) to do so.


## Reserve and log in to resources on CloudLab

For this experiment, we will use the CloudLab profile available at the following link: [https://www.cloudlab.us/p/cl-education/hello-linux](https://www.cloudlab.us/p/cl-education/hello-linux)

You'll see a brief description of the profile:

![Description of profile.](images/profile-1.png)

Click "Next". On the following page, you'll see a diagram of your experiment topology (on the right - in this case, a single host named "romeo"),
and on the left you'll be asked to select the "Cluster" on which you want your experiment to run:

![Cluster selection.](images/profile-3.png)

Unless otherwise specified, these experiments can run on any cluster. However, since CloudLab is a shared resource, on some occasionas the cluster you select might not have enough available resources to support your experiment. The status indicator next to each cluster tells you roughly how heavily utilized it is at the moment - green indicates that there are not many users, orange means heavy load, and red means that it is almost fully utilized. You are more likely to be successful if you choose a cluster with a green indicator.

After you select a cluster, you can leave the "Name" field blank, or give your experiment a name - it's your choice. Also make sure your "Project" is selected. Then, click "Next".

![Set experiment duration.](images/profile-4.png)

On the last page, you'll be asked to set the duration of your experiment. At the end of this duration, your resources will be deleted automatically - so make sure to give yourself enough time to finish.

You can leave the start date/time on this page blank if you are ready to work on the experiment right now. 

When you have made all your choices, click "Finish" to ask CloudLab to reserve resources according to your configuration.

### Exercise - Wait for resources to be ready 

Once you have successfully instantiated a profile, it will still take some time before your resources are ready for you to log in.

As your resources come online, you'll see their progress on the CloudLab experiment page:

![Instantiation progress.](images/instantiate-0.png)

As time passes, you will see a diagram of your experiment, but initially the hosts in the experiment will be colored yellow - this indicates that they're not ready to use yet. There's also a small "⊝" icon in the top right corner of the host - this indicates that it is not yet fully configured.

![Instantiation progress.](images/instantiate-1.png)

It can take a while for hosts to boot up and load their configurations - you may want to step away or work on something else for 15-20 minutes and then check back.

At some point, the host will turn green, but it may have a "⊙" icon in the top right - this indicates that it is still being configured.

![Instantiation progress.](images/instantiate-2.png)


Eventually, the host will be "green" with a "✓" icon in the top right corner. This shows that it is ready to use, and you can go on to the next step.

![Instantiation complete.](images/instantiate-3.png)

> **What if it fails?** If the CloudLab site is unable to bring up the resources you requested, the hosts will turn red instead of green. If this happens, delete the resources (use the red "Terminate" button). Then, try to reserve your resources again - you may want to try a different cluster, in case the problem was with the specific cluster that you used.

### Exercise - Log in to resources

Once the host in your experiment is "green" and has a "✓" icon in the top right corner, it is ready for you to log in! In this exercise, you'll practice accessing the host three ways:

* Using the terminal in the CloudLab web portal
* Using your own terminal application
* Using VNC (for a graphical interface)

---

<small>Questions about this material? Contact Fraida Fund</small>

---

<small>This material is based upon work supported by the National Science Foundation under Grant No. 2231984.</small>
<small>Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.</small>
