from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/media/hfc/HFCDS/lib/202206/Stark/data/got10k_lmdb'
    settings.got10k_path = '/media/hfc/HFCDS/lib/202206/Stark/data/got10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.lasot_lmdb_path = '/media/hfc/HFCDS/lib/202206/Stark/data/lasot_lmdb'
    settings.lasot_path = '/media/hfc/HFCDS/lib/202206/Stark/data/lasot'
    settings.network_path = '/media/hfc/HFCDS/lib/202206/Stark/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/media/hfc/HFCDS/lib/202206/Stark/data/nfs'
    settings.otb_path = '/media/hfc/HFCDS/lib/202206/Stark/data/OTB2015'
    settings.prj_dir = '/media/hfc/HFCDS/lib/202206/Stark'
    settings.result_plot_path = '/media/hfc/HFCDS/lib/202206/Stark/test/result_plots'
    settings.results_path = '/media/hfc/HFCDS/lib/202206/Stark/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/media/hfc/HFCDS/lib/202206/Stark'
    settings.segmentation_path = '/media/hfc/HFCDS/lib/202206/Stark/test/segmentation_results'
    settings.tc128_path = '/media/hfc/HFCDS/lib/202206/Stark/data/TC128'
    settings.tn_packed_results_path = ''
    settings.tpl_path = ''
    settings.trackingnet_path = '/media/hfc/HFCDS/lib/202206/Stark/data/trackingNet'
    settings.uav_path = '/media/hfc/HFCDS/lib/202206/Stark/data/UAV123'
    settings.vot_path = '/media/hfc/HFCDS/lib/202206/Stark/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

