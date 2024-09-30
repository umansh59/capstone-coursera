import matplotlib.pyplot as plt

def plot_model_vs_baseline(model_metrics, baseline_metrics):
    plt.figure(figsize=(10, 5))
    plt.plot(model_metrics, label='Model')
    plt.plot(baseline_metrics, label='Baseline')
    plt.legend()
    plt.title('Model vs. Baseline Performance')
    plt.show()

if __name__ == '__main__':
    model_metrics = [0.8, 0.85, 0.83]
    baseline_metrics = [0.7, 0.75, 0.74]
    plot_model_vs_baseline(model_metrics, baseline_metrics)
