import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'text.usetex':True,
    'font.family':'serif',
    # 'font.sans-serif': 'Helvetica',
})

def plots(filename, dt, columns='all'):
    with open(filename) as f:
        headers = f.readline().strip().split()
        if columns == 'all':
            columns = list(range(len(headers)))
        elif columns != 'all':
            headers = [headers[i] for i in columns]
        values = [[] for i in columns]
        for line in f:
            line = line.strip().split()
            for i in range(len(columns)):
                values[i].append(float(line[columns[i]]))
    
    Time = np.array(values[0])*dt
    if filename.startswith('eq'):
        prefix = 'eq'
    elif filename.startswith('nonEq'):
        prefix = 'nonEq'
    for i in range(1, len(headers)):
        fig = plt.figure(figsize=(6, 6), constrained_layout=True)
        gs = fig.add_gridspec(1, 1)
        ax = fig.add_subplot(gs[0, 0])
        ax.set_xlabel('Time, (---)')
        ax.set_ylabel(f'{headers[i]}, (---)')
        ax.plot(Time, values[i], marker='o', markersize=.5, color='deepskyblue', label=headers[i])
        ax.legend()
        fig.savefig(prefix + f'{headers[i]}' + '.png', dpi=300)
        plt.cla()
        plt.close('all')
    return None


if __name__ == "__main__":
    plots('eqResults.dat', 1e-2, 'all')
    plots('nonEqResults.dat', 1e-2, 'all')
