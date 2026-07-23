import React from 'react';

function PredictionResult({ prediction, formatCurrency, isCustom }) {
  return (
    <div className="prediction-result">
      <div className="result-header">
        <h3>🎯 Prediction Results</h3>
        <span className="confidence-badge">{prediction.confidence}% Confidence</span>
      </div>

      <div className="timeline-hero">
        <div className="timeline-stat">
          <span className="stat-number">{prediction.monthsToCompletion}</span>
          <span className="stat-label">Months to Goal</span>
        </div>
        <div className="timeline-stat">
          <span className="stat-number">{prediction.weeksToCompletion}</span>
          <span className="stat-label">Weeks Total</span>
        </div>
        <div className="timeline-stat">
          <span className="stat-number">{prediction.totalHours}</span>
          <span className="stat-label">Hours Needed</span>
        </div>
      </div>

      <div className="completion-date">
        🎉 Estimated completion: <strong>{prediction.completionDate}</strong>
      </div>

      <div className="milestones-section">
        <h4>📍 Your Learning Milestones</h4>
        <div className="milestones">
          {prediction.milestones.map((milestone, i) => (
            <div key={i} className="milestone-card">
              <div className="milestone-marker">
                <span className="milestone-number">{i + 1}</span>
                <div className="milestone-line"></div>
              </div>
              <div className="milestone-content">
                <div className="milestone-header">
                  <h5>{milestone.name}</h5>
                  <span className="milestone-weeks">Week {milestone.weeks}</span>
                </div>
                <p>{milestone.description}</p>
                <div className="milestone-progress">
                  <div className="progress-bar">
                    <div className="progress-fill" style={{ width: `${milestone.percentage}%` }}></div>
                  </div>
                  <span className="progress-text">{milestone.percentage}%</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="insights-grid">
        <div className="insight-card">
          <h4>📈 Market Insights</h4>
          <div className="market-stats">
            <div className="market-stat">
              <span className="stat-label">Demand</span>
              <span className="stat-value demand-high">{prediction.marketInsights.demand}</span>
            </div>
            <div className="market-stat">
              <span className="stat-label">Growth</span>
              <span className="stat-value">{prediction.marketInsights.growth}</span>
            </div>
            <div className="market-stat">
              <span className="stat-label">Competition</span>
              <span className="stat-value">{prediction.marketInsights.competition}</span>
            </div>
          </div>
        </div>

        <div className="insight-card">
          <h4>💰 Salary Projections</h4>
          <div className="salary-tiers">
            <div className="salary-tier entry"><span className="tier-label">Entry</span><span className="tier-salary">{formatCurrency(prediction.salaryProjection.entry)}</span></div>
            <div className="salary-tier mid"><span className="tier-label">Mid</span><span className="tier-salary">{formatCurrency(prediction.salaryProjection.mid)}</span></div>
            <div className="salary-tier senior"><span className="tier-label">Senior</span><span className="tier-salary">{formatCurrency(prediction.salaryProjection.senior)}</span></div>
          </div>
        </div>
      </div>

      <div className="factors-section">
        <div className="factors-column">
          <h4>✅ Speed Up Factors</h4>
          {prediction.speedUpFactors.length > 0 ? (
            <ul className="factors-list speed-up">
              {prediction.speedUpFactors.map((factor, i) => (<li key={i}><span className="check">✓</span> {factor}</li>))}
            </ul>
          ) : <p className="no-factors">Add more projects and find a mentor!</p>}
        </div>
        <div className="factors-column">
          <h4>⚠️ Slow Down Factors</h4>
          {prediction.slowDownFactors.length > 0 ? (
            <ul className="factors-list slow-down">
              {prediction.slowDownFactors.map((factor, i) => (<li key={i}><span className="warning">!</span> {factor}</li>))}
            </ul>
          ) : <p className="no-factors success">Great! No major slowdowns.</p>}
        </div>
      </div>
    </div>
  );
}


export default PredictionResult;