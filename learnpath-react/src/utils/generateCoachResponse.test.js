import generateCoachResponse from './generateCoachResponse';

// Minimal valid context shape — see the `ctx.*` fields generateCoachResponse
// reads. Individual tests override only what they need.
const baseParams = {
  ctx: {
    pathTopic: null,
    quizScores: [],
    weakAreas: [],
    strongAreas: [],
    enrolledCount: 0,
    learningPathLength: 0,
  },
  goal: 'web',
  hours: 2,
  experience: 0,
  enrolledCourses: [],
};

describe('generateCoachResponse', () => {
  test('returns a non-empty string for any question', () => {
    const response = generateCoachResponse('hello', baseParams);
    expect(typeof response).toBe('string');
    expect(response.length).toBeGreaterThan(0);
  });

  test('matches the motivation/burnout branch on relevant keywords', () => {
    const response = generateCoachResponse('I feel so burnout lately', baseParams);
    expect(response.toLowerCase()).toMatch(/motivation|marathon|rest|break/);
  });

  test('matches the schedule/planning branch', () => {
    const response = generateCoachResponse('How should I structure my daily schedule?', baseParams);
    expect(response.toLowerCase()).toMatch(/schedule|plan|daily/);
  });

  test('matches the projects branch', () => {
    const response = generateCoachResponse('What projects should I build?', baseParams);
    expect(response.toLowerCase()).toMatch(/project|portfolio|build/);
  });

  test('matches the Python-specific branch', () => {
    const response = generateCoachResponse('Any tips for learning Python?', baseParams);
    expect(response.toLowerCase()).toContain('python');
  });

  test('matches the interview/career branch', () => {
    const response = generateCoachResponse('How do I prepare for a job interview?', baseParams);
    expect(response.toLowerCase()).toMatch(/interview|career|job/);
  });

  test('falls back to general advice for an unrecognized question', () => {
    const response = generateCoachResponse('asdkfjaslkdfj', baseParams);
    expect(response).toMatch(/Top Advice|Consistency/);
  });

  test('does not throw when ctx has weak/strong areas populated', () => {
    const params = {
      ...baseParams,
      ctx: {
        ...baseParams.ctx,
        weakAreas: ['SQL'],
        strongAreas: ['Python'],
        pathTopic: 'Data Science',
      },
    };
    expect(() => generateCoachResponse('How is my progress?', params)).not.toThrow();
  });
});
