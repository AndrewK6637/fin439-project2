# My check of my partner's Project 2 app

This records my later check of my partner's app. It is separate from a partner cold run of my own repository and from my AI-off changed-input experiment.

| Item | What I observed |
| --- | --- |
| Partner project | [VISA-Research-NEW, Project-2 on `lab-20-readiness`](https://github.com/aidanklebenow/VISA-Research-NEW/tree/lab-20-readiness/Project-2) |
| Date | 11/19/2026 (confirmed by Aidan's email) |
| Start and duration | 9:40 EST; approximately 15 minutes |
| First README command attempted | `python3 Project-2/model.py` from the repository root |
| First failure | “Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.” |
| Command that worked | `py -3.14 Project-2/model.py` using the installed Python 3.14 launcher |
| Decision found | Keep the portfolio for research; hold off on investing client money. |
| Best candidate shown | 55% SGOV, 30% VTI, 15% VXUS; modeled annual return 7.5% and estimated volatility 6.8%, below the proposed 10% limit. It was the only portfolio shown as passing the model checks. The other two fell short of the return target. |
| Reason for holding off | Client risk limits and withdrawal schedule need verification. Application of the 7% issuer limit to fund holdings and Treasuries needs clarification. |
| Input I changed | Annual return target: 7.5% to 10%. |
| Output after the change | More U.S. stocks and less short-term Treasuries; modeled return 10.01%; estimated volatility rose from 6.80% to 10.84%. The displayed candidate changed from pass to fail because volatility exceeded the proposed 10% limit. |
| Was the input restored? | Not recorded. |
| Assistance used | I used Codex for much of the process of opening the app through GitHub. This was an AI-assisted check. |

## Question for my partner

When I raised the annual return target to 10%, why did the app show a portfolio that exceeded the 10% volatility limit? How does the code decide what to show when it cannot find a portfolio that meets both targets?

**Partner's answer (from Aidan's email):** His app first finds the lowest-volatility portfolio that reaches the return target while keeping the minimum SGOV cash reserve. It then checks that candidate against the separate 10% volatility limit. At a 10% return target, the safest mix that met the return target and SGOV reserve had 10.84% volatility, so his app displayed it as **FAIL**. That lets the committee see why the target and risk limit cannot both be met. If no mix reaches the return target at all, his app displays only the two comparison portfolios and a **STOP** message.

In plain terms, his 10% case had a candidate that met return and reserve but failed the risk limit. My separate locked 85% BIL-floor test returned **no feasible portfolio** that met both the reserve floor and 5.50% return hurdle; Aidan's description of when his app shows **STOP** is the closer comparison. These are different apps and different tests. Aidan changed no inputs during his cold run of my Cedar app; my 10% target change was during my check of his app.
