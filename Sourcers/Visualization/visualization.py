import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random
import os
#-----------------------------------------
# Plot Builder
#-----------------------------------------

class PlotBuilder:
    def __init__(self, df=None):
        self.df = df
        self.palette1 = "light:#5A9"
        self.palette2 = "Set2"

    def _random_color(self):
        return random.choice(sns.color_palette("tab10", 10))

    #-------------------------
    # Line Plot
    #-------------------------
    def line(self, x, y, title=None):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(self.df[x], self.df[y], color=self._random_color())
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        if title:
            ax.set_title(title)
        return fig

    #-------------------------
    # Histogram
    #-------------------------
    def hist(self, column, bins=30, title=None):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(self.df[column], bins=bins, color=self._random_color())
        ax.set_xlabel(column)
        if title:
            ax.set_title(title)
        return fig

    #-------------------------
    # Boxplot
    #-------------------------
    def box(self, column, by=None, title=None):
        fig, ax = plt.subplots(figsize=(10, 6))
        if by:
            sns.boxplot(x=self.df[by], y=self.df[column], ax=ax, palette=self.palette1)
        else:
            ax.boxplot(self.df[column].dropna())
        if title:
            ax.set_title(title)
        return fig

    #-------------------------
    # Violin Plot
    #-------------------------
    def violin(self, column, by=None, title=None):
        fig, ax = plt.subplots(figsize=(10, 6))
        if by:
            sns.violinplot(x=self.df[by], y=self.df[column], ax=ax, palette=self.palette2)
        else:
            sns.violinplot(y=self.df[column], ax=ax, palette=self.palette)
        if title:
            ax.set_title(title)
        return fig

    #-------------------------
    # Scatter Plot
    #-------------------------
    def scatter(self, x, y, title=None):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(self.df[x], self.df[y], color=self._random_color())
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        if title:
            ax.set_title(title)
        return fig

    #-------------------------
    # Bar Plot
    #-------------------------
    def bar(self, x, y, title=None, horizontal=False):
        fig, ax = plt.subplots(figsize=(10, 6))

        if horizontal:
            ax.barh(self.df[x], self.df[y], color=self._random_color())
            ax.set_ylabel(x)
            ax.set_xlabel(y)
        else:
            ax.bar(self.df[x], self.df[y], color=self._random_color())
            ax.set_xlabel(x)
            ax.set_ylabel(y)

        if title:
            ax.set_title(title)
        return fig

    #-------------------------
    # Heatmap
    #-------------------------
    def heatmap(self, title=None, annot=False):
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(self.df, cmap='viridis', annot=annot, ax=ax)
        if title:
            ax.set_title(title)
        return fig

    #-------------------------
    # Pairplot
    #-------------------------
    def pairplot(self, hue=None, diag_kind="kde", title=None):
        grid = sns.pairplot(
            self.df,
            hue=hue,
            diag_kind=diag_kind,
            palette=self.palette2,
            corner=True,
            plot_kws={"alpha": 0.6, "s": 40}
        )

        if title:
            grid.fig.suptitle(title, y=1.02)

        return grid.fig

    #-------------------------
    # Multi-Boxplot (subplot)
    #-------------------------
    def multi_boxplot(self, columns, by, title=None):
        n = len(columns)
        rows = (n // 3) + (1 if n % 3 != 0 else 0)
        fig, axes = plt.subplots(rows, 3, figsize=(18, 5 * rows))
        axes = axes.flatten()
        for ax, col in zip(axes, columns):
            sns.boxplot(
                data=self.df,
                x=by,
                y=col,
                palette=self.palette1,
                showfliers=False,
                ax=ax
            )
            ax.set_title(f"{col} by {by}", fontsize=11, fontweight="bold")
            ax.tick_params(axis="x", rotation=25)
        for i in range(len(columns), len(axes)):
            axes[i].set_visible(False)
        if title:
            fig.suptitle(title, fontsize=15, fontweight="bold", y=1.02)
        fig.tight_layout()
        return fig

#-----------------------------------------
# Export Figures
#-----------------------------------------

class FigureExporter:
    def __init__(self, fig):
        self.fig = fig

    def save(self, path, dpi=300):
        self.fig.savefig(path, dpi=dpi, bbox_inches="tight")
        plt.close(self.fig)
        return path


#-----------------------------------------
# Exxport DataFrames or dicts as cvs or png
#-----------------------------------------

class TableExporter:
    def __init__(self, table):
        if isinstance(table, pd.DataFrame):
            self.table = table
        else:
            self.table = pd.DataFrame(table)

    def to_csv(self, folder_path, filename):
        os.makedirs(folder_path, exist_ok=True)
        fullpath = os.path.join(folder_path, filename)
        self.table.to_csv(fullpath, index=True)
        return fullpath

    def to_png(self, path, dpi=300):
        fig, ax = plt.subplots(figsize=(12, 2 + 0.3 * len(self.table)))
        ax.axis("off")
        table = ax.table(
            cellText=self.table.values,
            colLabels=self.table.columns,
            loc="center"
        )
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 1.5)

        fig.savefig(path, dpi=dpi, bbox_inches="tight")
        plt.close(fig)
        return path