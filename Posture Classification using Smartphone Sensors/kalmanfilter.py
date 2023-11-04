from pykalman import KalmanFilter
import pandas as pd

def Kalman1D(observations,damping=1):
    # To return the smoothed time series data
    observation_covariance = damping
    initial_value_guess = observations[0]
    transition_matrix = 1
    transition_covariance = 0.1
    initial_value_guess

    kf = KalmanFilter(
            initial_state_mean=initial_value_guess,
            initial_state_covariance=observation_covariance,
            observation_covariance=observation_covariance,
            transition_covariance=transition_covariance,
            transition_matrices=transition_matrix
        )

    pred_state, _ = kf.smooth(observations)

    return pred_state

def update_dataset(df: pd.DataFrame):
    for col in df.columns:
        if col == "timestamp": continue

        df[col] = Kalman1D(df[col].values, 1)

    return df

if __name__ == "__main__":
    df = pd.read_csv("data/data_agg.csv")

    df = update_dataset(df)

    df.to_csv("data/data_agg_Kalman_filtered.csv", index=False)


