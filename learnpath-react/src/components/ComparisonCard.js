import React from 'react';

function ComparisonCard({ title, prediction, formatCurrency, isImproved }) {
  return (
    <div className={`comparison-card ${isImproved ? 'improved' : ''}`}>
      <h4>{title}</h4>
      <div className="comparison-stats">
        <div className="comp-stat"><span className="comp-label">Timeline</span><span className="comp-value">{prediction.monthsToCompletion} months</span></div>
        <div className="comp-stat"><span className="comp-label">Weekly Hours</span><span className="comp-value">{prediction.weeklyHours}h/week</span></div>
        <div className="comp-stat"><span className="comp-label">Total Hours</span><span className="comp-value">{prediction.totalHours}h</span></div>
      </div>
    </div>
  );
}


export default ComparisonCard;