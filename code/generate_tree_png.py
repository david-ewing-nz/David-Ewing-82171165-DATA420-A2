"""
Generate PNG image of MSD directory tree structure
Saves to: report/supplementary/msd_directory_tree.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def create_tree_png():
    """Create a PNG visualization of the MSD directory tree"""
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 16))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # Title
    ax.text(0.5, 49, 'MSD Dataset Directory Structure', 
            fontsize=16, fontweight='bold', family='monospace')
    
    # Directory tree text
    tree_text = '''└── msd/
    ├── audio/
    │   ├── attributes/
    │   │   ├── msd-jmir-area-of-moments-all-v1.0.attributes.csv
    │   │   ├── msd-jmir-lpc-all-v1.0.attributes.csv
    │   │   ├── msd-jmir-methods-of-moments-all-v1.0.attributes.csv
    │   │   ├── msd-jmir-mfcc-all-v1.0.attributes.csv
    │   │   ├── msd-jmir-spectral-all-v1.0.attributes.csv
    │   │   ├── msd-jmir-spectral-derivatives-all-v1.0.attributes.csv
    │   │   ├── msd-marsyas-timbral-v1.0.attributes.csv
    │   │   ├── msd-mvd-v1.0.attributes.csv
    │   │   ├── msd-rh-v1.0.attributes.csv
    │   │   ├── msd-rp-v1.0.attributes.csv
    │   │   ├── msd-ssd-v1.0.attributes.csv
    │   │   ├── msd-trh-v1.0.attributes.csv
    │   │   └── msd-tssd-v1.0.attributes.csv
    │   ├── features/
    │   │   ├── msd-jmir-area-of-moments-all-v1.0.csv/
    │   │   ├── msd-jmir-lpc-all-v1.0.csv/
    │   │   ├── msd-jmir-methods-of-moments-all-v1.0.csv/
    │   │   ├── msd-jmir-mfcc-all-v1.0.csv/
    │   │   ├── msd-jmir-spectral-all-v1.0.csv/
    │   │   ├── msd-jmir-spectral-derivatives-all-v1.0.csv/
    │   │   ├── msd-marsyas-timbral-v1.0.csv/
    │   │   ├── msd-mvd-v1.0.csv/
    │   │   ├── msd-rh-v1.0.csv/
    │   │   ├── msd-rp-v1.0.csv/
    │   │   ├── msd-ssd-v1.0.csv/
    │   │   ├── msd-trh-v1.0.csv/
    │   │   └── msd-tssd-v1.0.csv/
    │   └── statistics/
    │       └── sample_properties.csv.gz
    ├── genre/
    │   ├── msd-MAGD-genreAssignment.tsv
    │   ├── msd-MASD-styleAssignment.tsv
    │   └── msd-topMAGD-genreAssignment.tsv
    ├── main/
    │   └── summary/
    │       ├── analysis.csv.gz
    │       └── metadata.csv.gz
    └── tasteprofile/
        ├── mismatches/
        │   ├── sid_matches_manually_accepted.txt
        │   └── sid_mismatches.txt
        └── triplets.tsv'''
    
    # Add the tree text
    ax.text(0.5, 47, tree_text, fontsize=9, family='monospace', 
            verticalalignment='top', linespacing=1.5)
    
    # Save the figure
    output_path = 'report/supplementary/msd_directory_tree.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f'[info] Successfully saved: {output_path}')
    return output_path

if __name__ == '__main__':
    create_tree_png()
